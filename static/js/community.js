const API_BASE = "/api/community";
let currentFilter = "All Topics";

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
    container.innerHTML = "<p style='text-align:center; color:#9ca3af; margin-top:20px'>Loading discussions...</p>";
    
    let url = `${API_BASE}/posts?sort=${sortOrder}`;
    if (tag && tag !== "All Topics") url += `&tag=${encodeURIComponent(tag)}`;

    try {
        const res = await fetch(url);
        const posts = await res.json();
        container.innerHTML = "";
        const userVotes = getStorageObj('user_votes');

        posts.forEach(post => {
            const voteStatus = userVotes[post.id];
            const agreeClass = voteStatus === 'agree' ? 'active' : '';
            const disagreeClass = voteStatus === 'disagree' ? 'active' : '';
            const commentCount = post.comment_count !== undefined ? post.comment_count : 0;
            
            const card = document.createElement('div');
            card.className = 'post-card';
            card.innerHTML = `
                <div class="post-meta">
                    <span style="font-weight:700; color:var(--deep-blue)">${escapeHtml(post.teacher_name)}</span> • <span class="badge-tag">${post.tag}</span> • <span>Just now</span>
                </div>
                <h4 class="post-title">${escapeHtml(post.title)}</h4>
                <p class="post-body">${escapeHtml(post.content)}</p>
                <div class="action-bar">
                    <button class="btn-vote vote-agree ${agreeClass}" onclick="handleVote(${post.id}, 'agree')">👍 Agree ${post.likes}</button>
                    <button class="btn-vote vote-disagree ${disagreeClass}" onclick="handleVote(${post.id}, 'disagree')">👎 Disagree ${post.disagrees || 0}</button>
                    <button class="btn-text" onclick="toggleComments(${post.id})">💬 ${commentCount} Comments</button>
                    <button class="btn-text" onclick="sharePost(${post.id})">🔗 Share</button>
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

async function loadComments(postId) {
    const listContainer = document.getElementById(`comment-list-${postId}`);
    const res = await fetch(`${API_BASE}/posts/${postId}/comments`);
    const comments = await res.json();
    const commentMap = {};
    const roots = [];
    comments.forEach(c => { c.children = []; commentMap[c.id] = c; });
    comments.forEach(c => {
        if (c.parent_id && commentMap[c.parent_id]) {
            commentMap[c.parent_id].children.push(c);
            c.parentAuthor = commentMap[c.parent_id].author;
        } else { roots.push(c); }
    });
    listContainer.innerHTML = roots.map(c => renderCommentNode(c, postId)).join('');
}

function renderCommentNode(comment, postId) {
    const replyingTo = comment.parentAuthor ? `<span class="replying-to">replying to ${escapeHtml(comment.parentAuthor)}</span>` : '';
    return `
    <div class="comment-node">
        <div class="comment-bubble">
            <div class="comment-header">${escapeHtml(comment.author)} ${replyingTo}</div>
            <div style="font-size:0.9rem">${escapeHtml(comment.text)}</div>
            <span class="reply-link" onclick="toggleReplyBox(${comment.id})">Reply</span>
        </div>
        <div id="reply-box-${comment.id}" class="reply-input-box">
            <input type="text" id="input-reply-${comment.id}" placeholder="Reply...">
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
    loadComments(postId); loadPosts(currentFilter);
}

async function handleVote(postId, newVoteType) {
    const userVotes = getStorageObj('user_votes');
    const currentVote = userVotes[postId]; 
    const action = (currentVote === newVoteType) ? `remove_${newVoteType}` : `add_${newVoteType}`;
    if (currentVote && currentVote !== newVoteType) {
        await fetch(`${API_BASE}/posts/${postId}/vote`, { method: 'POST', body: JSON.stringify({ action: `remove_${currentVote}` }), headers: {'Content-Type': 'application/json'} });
    }
    if (action.startsWith("remove")) delete userVotes[postId];
    else userVotes[postId] = newVoteType;
    
    setStorageObj('user_votes', userVotes);
    await fetch(`${API_BASE}/posts/${postId}/vote`, { method: 'POST', body: JSON.stringify({ action }), headers: {'Content-Type': 'application/json'} });
    loadPosts(currentFilter);
}

async function submitPost() {
    const title = document.getElementById('postTitle').value;
    const content = document.getElementById('postContent').value;
    let tag = document.getElementById('postTagInput').value || "General";
    if (!title || !content) return alert("Write something!");
    await fetch(`${API_BASE}/posts`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ title, content, tag }) });
    document.getElementById('postTitle').value = "";
    document.getElementById('postContent').value = "";
    await loadTags(); await loadPosts(currentFilter);
}

async function sharePost(id) {
    navigator.clipboard.writeText(window.location.origin + "/community");
    alert("Link copied!");
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
        li.onclick = () => { currentFilter = tag; loadPosts(tag); document.querySelectorAll('li').forEach(el=>el.classList.remove('active')); li.classList.add('active'); };
        list.appendChild(li);
        if(tag !== "All Topics") { const opt = document.createElement('option'); opt.value = tag; datalist.appendChild(opt); }
    });
}
