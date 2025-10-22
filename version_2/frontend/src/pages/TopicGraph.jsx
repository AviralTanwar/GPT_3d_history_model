import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { DataContext } from "../App";

export default function TopicGraph(){
  const { conversations } = useContext(DataContext);
  if(!conversations){
    return (
      <div className="app-shell">
        <div className="sidebar"/>
        <main className="main">
          <div className="card">
            <h1>No data loaded</h1>
            <p>Please go back and choose your <b>conversations.json</b>.</p>
            <Link to="/"><button className="primary">Go to Upload</button></Link>
          </div>
        </main>
      </div>
    );
  }
  const count = Array.isArray(conversations) ? conversations.length : 0;
  const sample = conversations?.[0]?.title ?? "Untitled";
  return (
    <div className="app-shell">
      <div className="sidebar">
        <h2>🪐 Topic Graph</h2>
        <ol>
          <li>Data loaded in memory</li>
          <li>Next: render 3D graph / filters</li>
        </ol>
      </div>
      <main className="main">
        <div className="card">
          <h1>Data ready ✅</h1>
          <p>Items: <b>{count}</b></p>
          <p>First title: <span className="mono">{sample}</span></p>
          <Link to="/"><button className="primary">Back</button></Link>
        </div>
      </main>
    </div>
  );
}
