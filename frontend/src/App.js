import React from "react";
import TriggerTable from "./TriggerTable";
import "antd/dist/reset.css"; // för Ant Design styling i v5+
import "./App.css";
import {Card} from "antd";

function App() {
  return (
      <div className="App" style={{ padding: 24 }}>
          <Card title="Aktie-triggers" style={{ marginBottom: 24 }}>
              <TriggerTable />
          </Card>
      </div>
  );
}

export default App;
