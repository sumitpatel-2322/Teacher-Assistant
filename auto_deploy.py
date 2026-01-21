import os
import re

print("📍 Relocating Community Button to under Profile...")

sidebar_path = os.path.join("templates", "Partials", "sidebar.html")

# The Standard Community Button HTML (Cleanly formatted)
community_btn_html = """
        <a href="/community" class="nav-link">
            <span class="icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
            </span>
            <span class="text">Community</span>
        </a>"""

try:
    if os.path.exists(sidebar_path):
        with open(sidebar_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Step 1: Remove ANY existing Community link (to avoid duplicates)
        # Regex matches <a href="/community" ... </a> inclusive, handling newlines
        clean_content = re.sub(r'\s*<a href="/community".*?</a>', '', content, flags=re.DOTALL)

        # Step 2: Find the Profile Link to insert after
        # Looking for the standard profile link structure
        profile_marker = 'href="/profile"'
        
        if profile_marker in clean_content:
            # Split the content at the Profile link
            # We need to find where the Profile <a> tag ENDS
            parts = clean_content.split(profile_marker)
            
            # parts[0] is before href="/profile"
            # parts[1] is the rest. We need to find the closing </a> in parts[1]
            
            rest_of_sidebar = parts[1]
            closing_tag_index = rest_of_sidebar.find('</a>') + 4 # +4 for the length of </a>
            
            # Reconstruct:
            # 1. Everything up to Profile href
            # 2. The Profile href itself
            # 3. The rest of the Profile anchor tag (up to </a>)
            # 4. NEW LINE + COMMUNITY BUTTON
            # 5. The rest of the file
            
            new_sidebar = (
                parts[0] + 
                profile_marker + 
                rest_of_sidebar[:closing_tag_index] + 
                "\n" + community_btn_html + 
                rest_of_sidebar[closing_tag_index:]
            )
            
            with open(sidebar_path, "w", encoding="utf-8") as f:
                f.write(new_sidebar)
            print("✅ Success! Moved 'Community' button directly under 'Profile'.")
            
        else:
            print("⚠️ Could not find 'Profile' link. Appending to end of list instead.")
            # Fallback: Insert before Logout if Profile isn't found
            if 'href="/logout"' in clean_content:
                new_sidebar = clean_content.replace('href="/logout"', f'href="/logout"').replace('<a href="/logout"', f'{community_btn_html}\n        <a href="/logout"')
                with open(sidebar_path, "w", encoding="utf-8") as f:
                    f.write(new_sidebar)
                print("✅ Placed before Logout (Profile not found).")

    else:
        print(f"❌ Error: {sidebar_path} not found.")

except Exception as e:
    print(f"❌ Error: {e}")