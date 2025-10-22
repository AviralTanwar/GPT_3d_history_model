import React from "react";
import SidebarInstructions from "../components/SidebarInstructions";
import UploadPanel from "../components/UploadPanel";

export default function Home(){
  return (
    <div className="app-shell">
      <SidebarInstructions />
      <main className="main">
        <UploadPanel />
      </main>
    </div>
  );
}
