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
    container.innerHTML = "<p style='text-align:center; color:#6b7280; margin-top:20px'>Loading VEDA community...</p>";
    
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
                    <span style="font-weight:700; color:var(--text-main)">${escapeHtml(post.teacher_name)}</span> • <span class="badge-tag">${post.tag}</span> • <span>Just now</span>
                </div>
                <h4 class="post-title">${escapeHtml(post.title)}</h4>
                <p class="post-body">${escapeHtml(post.content)}</p>
                
                <div class="action-bar">
                    <button class="btn-vote vote-agree ${agreeClass}" onclick="handleVote(${post.id}, 'agree')">
                         Agree ${post.likes}
                    </button>
                    <button class="btn-vote vote-disagree ${disagreeClass}" onclick="handleVote(${post.id}, 'disagree')">
                         Disagree ${post.disagrees || 0}
                    </button>
                    <button class="btn-vote" style="background:transparent;" onclick="toggleComments(${post.id})">
                         💬 ${commentCount} Comments
                    </button>
                    <button class="btn-vote" style="background:transparent; margin-left:auto;" onclick="sharePost(${post.id})">
                         🔗 Share
                    </button>
                </div>

                <div id="comments-${post.id}" class="comments-section" style="display:none; margin-top:15px; border-top:1px solid #eee; padding-top:10px;">
                    <div style="display:flex; gap:10px; margin-bottom:15px;">
                        <input type="text" id="input-${post.id}" placeholder="Write a reply..." style="margin-bottom:0;">
                        <button class="btn-primary" style="width:auto; padding:8px 20px;" onclick="submitComment(${post.id}, null)">Send</button>
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
    if(comments.length === 0) { listContainer.innerHTML = "<p style='font-size:0.8rem; color:grey;'>No comments yet.</p>"; return; }
    
    listContainer.innerHTML = comments.map(c => `
        <div class="comment-node" style="margin-bottom:10px; background:#f9fafb; padding:10px; border-radius:8px;">
            <div class="comment-header" style="font-weight:bold; font-size:0.85rem; color:#056b64;">${escapeHtml(c.author)}</div>
            <div style="font-size:0.9rem">${escapeHtml(c.text)}</div>
        </div>
    `).join('');
}

async function submitComment(postId, parentId) {
    const input = document.getElementById(`input-${postId}`);
    if (!input.value) return;
    const formData = new FormData();
    formData.append("author", typeof USER_NAME !== 'undefined' ? USER_NAME : "Anonymous");
    formData.append("text", input.value);
    await fetch(`${API_BASE}/posts/${postId}/comments`, { method: 'POST', body: formData });
    input.value = "";
    loadComments(postId); loadPosts(currentFilter);
}

async function handleVote(postId, newVoteType) {
    const userVotes = getStorageObj('user_votes');
    const currentVote = userVotes[postId]; 
    const action = (currentVote === newVoteType) ? `remove_${newVoteType}` : `add_${newVoteType}`;
    
    // Optimistic UI Update (optional) or wait for reload
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
    if (!title || !content) return alert("Please fill in both title and content.");
    await fetch(`${API_BASE}/posts`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ title, content, tag }) });
    document.getElementById('postTitle').value = "";
    document.getElementById('postContent').value = "";
    await loadTags(); await loadPosts(currentFilter);
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
        li.onclick = () => { currentFilter = tag; loadPosts(tag); document.querySelectorAll('li').forEach(el=>el.classList.remove('active')); li.classList.add('active'); };
        list.appendChild(li);
        if(tag !== "All Topics") { const opt = document.createElement('option'); opt.value = tag; datalist.appendChild(opt); }
    });
}
