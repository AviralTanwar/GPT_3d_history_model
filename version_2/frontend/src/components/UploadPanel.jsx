import React, { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { DataContext } from "../App";

export default function UploadPanel(){
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");
  const navigate = useNavigate();
  const { setConversations } = useContext(DataContext);

  const readFile = () => {
    if(!file){ setStatus("Please choose conversations.json first."); return; }
    setStatus("Reading file…");
    const reader = new FileReader();
    reader.onerror = () => setStatus("❌ Failed to read file.");
    reader.onload = () => {
      try{
        const json = JSON.parse(reader.result);
        setConversations(json);
        try { sessionStorage.setItem("conversations_json", JSON.stringify(json)); } catch {}
        setStatus(`✅ Loaded ${Array.isArray(json) ? json.length : 0} items. Redirecting…`);
        navigate("/topic-graph");
      }catch{
        setStatus("❌ Invalid JSON file.");
      }
    };
    reader.readAsText(file);
  };

  return (
    <div className="card">
      <h1>📁 Upload ChatGPT JSON</h1>
      <p>Drop your <b>conversations.json</b> here. Processed entirely in your browser.</p>
      <div className="upload-row">
        <input type="file" accept="application/json,.json" onChange={(e)=>setFile(e.target.files?.[0] ?? null)} />
        <button className="primary" onClick={readFile}>Open</button>
      </div>
      <div className="status mono">{status}</div>
    </div>
  );
}
