import React from "react";
import TriggerTable from "./TriggerTable";
import "antd/dist/reset.css"; // för Ant Design styling i v5+
import "./App.css";
import {Card} from "antd";

function App() {
  return (
      <div style={{
          maxWidth: 1200,        // adjust as needed
          margin: "0 auto",      // center horizontally
          padding: "2rem",       // breathing room
          background: "#fff",    // optional: add card feel
      }}>
          <Card title="Aktie-triggers" style={{marginBottom: 24}}>
          <TriggerTable/>
      </Card>
      </div>
  );
}

export default App;
