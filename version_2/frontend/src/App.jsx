import React, { createContext, useMemo, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import TopicGraph from "./pages/TopicGraph";
import "./index.css";

export const DataContext = createContext(null);

export default function App() {
  // try to hydrate from sessionStorage if available
  const [conversations, setConversations] = useState(() => {
    try {
      const s = sessionStorage.getItem("conversations_json");
      return s ? JSON.parse(s) : null;
    } catch { return null; }
  });

  const ctx = useMemo(() => ({ conversations, setConversations }), [conversations]);

  return (
    <DataContext.Provider value={ctx}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/topic-graph" element={<TopicGraph/>} />
          <Route path="*" element={<Navigate to="/" replace/>} />
        </Routes>
      </BrowserRouter>
    </DataContext.Provider>
  );
}
