const API_BASE = "/api/community";
let currentFilter = "All Topics";

// Icons for dynamic injection
const ICONS = {
    thumb_up: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z"/></svg>',
    thumb_down: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"/></svg>',
    comment: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M21.99 4c0-1.1-.89-2-1.99-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4-.01-18zM18 14H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>',
    share: '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/></svg>'
};

// Utilities
function getStorageObj(key) { return localStorage.getItem(key) ? JSON.parse(localStorage.getItem(key)) : {}; }
function setStorageObj(key, obj) { localStorage.setItem(key, JSON.stringify(obj)); }
function escapeHtml(unsafe) {
    if (!unsafe) return "";
    return unsafe.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}

window.onload = async () => {
    await loadTags();
    await loadPosts(currentFilter);
};

function handleSortChange() { loadPosts(currentFilter); }

async function loadPosts(tag) {
    const container = document.getElementById('feed-container');
    const sortOrder = document.getElementById('sortOrder').value;
    container.innerHTML = "<p style='text-align:center; color:#9ca3af; margin-top:20px'>Loading community feed...</p>";
    
    let url = `${API_BASE}/posts?sort=${sortOrder}`;
    if (tag && tag !== "All Topics") url += `&tag=${encodeURIComponent(tag)}`;

    try {
        const res = await fetch(url);
        const posts = await res.json();
        container.innerHTML = "";
        const userVotes = getStorageObj('user_votes');

        if(posts.length === 0) {
            container.innerHTML = "<p style='text-align:center; padding:20px; color:#6b7280;'>No posts yet. Be the first to ask!</p>";
            return;
        }

        posts.forEach(post => {
            const voteStatus = userVotes[post.id];
            const agreeClass = voteStatus === 'agree' ? 'active' : '';
            const disagreeClass = voteStatus === 'disagree' ? 'active' : '';
            const commentCount = post.comment_count !== undefined ? post.comment_count : 0;
            
            const card = document.createElement('div');
            card.className = 'post-card';
            card.innerHTML = `
                <div class="post-meta">
                    <span style="font-weight:700; color:var(--text-main)">${escapeHtml(post.teacher_name)}</span> • <span class="badge-tag">${post.tag}</span> • <span>Recent</span>
                </div>
                <h4 class="post-title">${escapeHtml(post.title)}</h4>
                <p class="post-body">${escapeHtml(post.content)}</p>
                
                <div class="action-bar">
                    <button class="btn-vote vote-agree ${agreeClass}" onclick="handleVote(${post.id}, 'agree')">
                         ${ICONS.thumb_up} Agree ${post.likes}
                    </button>
                    <button class="btn-vote vote-disagree ${disagreeClass}" onclick="handleVote(${post.id}, 'disagree')">
                         ${ICONS.thumb_down} Disagree ${post.disagrees || 0}
                    </button>
                    <button class="btn-vote" style="background:transparent;" onclick="toggleComments(${post.id})">
                         ${ICONS.comment} ${commentCount} Comments
                    </button>
                    <button class="btn-vote" style="background:transparent; margin-left:auto;" onclick="sharePost(${post.id})">
                         ${ICONS.share} Share
                    </button>
                </div>

                <div id="comments-${post.id}" class="comments-section">
                    <div style="display:flex; gap:10px; margin-bottom:15px;">
                        <input type="text" id="input-${post.id}" placeholder="Write a reply..." style="margin-bottom:0;">
                        <button class="btn-small" onclick="submitComment(${post.id}, null)">Send</button>
                    </div>
                    <div id="comment-list-${post.id}"></div>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (e) { console.error(e); }
}

async function toggleComments(postId) {
    const section = document.getElementById(`comments-${postId}`);
    section.style.display = section.style.display === "block" ? "none" : "block";
    if (section.style.display === "block") loadComments(postId);
}

// --- CORE RECURSIVE FUNCTION FOR NESTED COMMENTS ---
async function loadComments(postId) {
    const listContainer = document.getElementById(`comment-list-${postId}`);
    const res = await fetch(`${API_BASE}/posts/${postId}/comments`);
    const comments = await res.json();
    
    if(comments.length === 0) { listContainer.innerHTML = "<p style='font-size:0.8rem; color:grey; font-style:italic;'>No comments yet.</p>"; return; }

    // Build Tree
    const commentMap = {};
    const roots = [];
    comments.forEach(c => { c.children = []; commentMap[c.id] = c; });
    comments.forEach(c => {
        if (c.parent_id && commentMap[c.parent_id]) {
            commentMap[c.parent_id].children.push(c);
            c.parentAuthor = commentMap[c.parent_id].author;
        } else { roots.push(c); }
    });
    
    // Render Tree
    listContainer.innerHTML = roots.map(c => renderCommentNode(c, postId)).join('');
}

// Recursive Renderer
function renderCommentNode(comment, postId) {
    const replyingTo = comment.parentAuthor ? `<span class="replying-to">replying to ${escapeHtml(comment.parentAuthor)}</span>` : '';
    
    return `
    <div class="comment-node">
        <div class="comment-bubble">
            <div class="comment-header">${escapeHtml(comment.author)} ${replyingTo}</div>
            <div style="font-size:0.9rem; margin-top:2px;">${escapeHtml(comment.text)}</div>
            <span class="reply-link" onclick="toggleReplyBox(${comment.id})">Reply</span>
        </div>
        
        <div id="reply-box-${comment.id}" class="reply-input-box">
            <input type="text" id="input-reply-${comment.id}" placeholder="Reply to ${escapeHtml(comment.author)}...">
            <button class="btn-small" onclick="submitComment(${postId}, ${comment.id})">Send</button>
        </div>
        
        <div class="comment-thread-line">
            ${comment.children.map(c => renderCommentNode(c, postId)).join('')}
        </div>
    </div>
    `;
}

function toggleReplyBox(id) {
    const box = document.getElementById(`reply-box-${id}`);
    box.style.display = box.style.display === "block" ? "none" : "block";
    if(box.style.display === "block") {
        const input = document.getElementById(`input-reply-${id}`);
        if(input) input.focus();
    }
}

async function submitComment(postId, parentId) {
    let inputId = parentId ? `input-reply-${parentId}` : `input-${postId}`;
    const input = document.getElementById(inputId);
    if (!input.value) return;
    
    const formData = new FormData();
    formData.append("author", typeof USER_NAME !== 'undefined' ? USER_NAME : "Anonymous");
    formData.append("text", input.value);
    if (parentId) formData.append("parent_id", parentId);
    
    await fetch(`${API_BASE}/posts/${postId}/comments`, { method: 'POST', body: formData });
    
    input.value = "";
    if (parentId) toggleReplyBox(parentId); 
    loadComments(postId); // Refresh comments to show new one
    // Also optionally refresh posts to update comment count
}

async function handleVote(postId, newVoteType) {
    const userVotes = getStorageObj('user_votes');
    const currentVote = userVotes[postId]; 
    const action = (currentVote === newVoteType) ? `remove_${newVoteType}` : `add_${newVoteType}`;
    
    if (currentVote && currentVote !== newVoteType) {
        // Remove old vote first
        await fetch(`${API_BASE}/posts/${postId}/vote`, { method: 'POST', body: JSON.stringify({ action: `remove_${currentVote}` }), headers: {'Content-Type': 'application/json'} });
    }
    if (action.startsWith("remove")) delete userVotes[postId];
    else userVotes[postId] = newVoteType;
    
    setStorageObj('user_votes', userVotes);
    await fetch(`${API_BASE}/posts/${postId}/vote`, { method: 'POST', body: JSON.stringify({ action }), headers: {'Content-Type': 'application/json'} });
    
    loadPosts(currentFilter); // Refresh UI
}

async function submitPost() {
    const title = document.getElementById('postTitle').value;
    const content = document.getElementById('postContent').value;
    let tag = document.getElementById('postTagInput').value || "General";
    
    if (!title || !content) return alert("Please fill in both title and content.");
    
    await fetch(`${API_BASE}/posts`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ title, content, tag }) });
    
    document.getElementById('postTitle').value = "";
    document.getElementById('postContent').value = "";
    
    await loadTags(); 
    await loadPosts(currentFilter);
}

async function sharePost(id) {
    navigator.clipboard.writeText(window.location.origin + "/community");
    alert("Link copied to clipboard!");
}

async function loadTags() {
    const res = await fetch(`${API_BASE}/tags`);
    const tags = await res.json();
    const list = document.getElementById('tag-list');
    const datalist = document.getElementById('tag-options');
    list.innerHTML = ""; datalist.innerHTML = "";
    
    tags.forEach(tag => {
        const li = document.createElement('li');
        li.textContent = tag;
        li.onclick = () => { 
            currentFilter = tag; 
            loadPosts(tag); 
            document.querySelectorAll('li').forEach(el=>el.classList.remove('active')); 
            li.classList.add('active'); 
        };
        list.appendChild(li);
        
        if(tag !== "All Topics") { 
            const opt = document.createElement('option'); 
            opt.value = tag; 
            datalist.appendChild(opt); 
        }
    });
}
