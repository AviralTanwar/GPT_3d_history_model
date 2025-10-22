import React from "react";

export default function SidebarInstructions(){
  return (
    <aside className="sidebar">
      <h2>📜 How to export your ChatGPT data</h2>
      <ol>
        <li>In ChatGPT → <b>Settings → Data Controls</b></li>
        <li>Click <b>Export data → Export</b></li>
        <li>Download the <code>.zip</code> from email</li>
        <li>Extract → find <b>conversations.json</b></li>
        <li>Upload it on the right to build the graph</li>
      </ol>
    </aside>
  );
}
