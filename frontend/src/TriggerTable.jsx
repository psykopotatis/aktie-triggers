// src/TriggerTable.jsx
import React, { useEffect, useState } from "react";
import { Table, Tag } from "antd"; // ✅ korrekt!


import axios from "axios";

const columns = [
    {
        title: "Aktie",
        dataIndex: "aktie",
        key: "aktie"
    },
    {
        title: "Beskrivning",
        dataIndex: "trigger_beskrivning",
        key: "beskrivning",
        render: (text, record) => (
            <div>
                <strong>{record.trigger_rubrik}</strong>
                <br />
                <span>{record.trigger_beskrivning}</span>
            </div>
        )
    },
    {
        title: "Påverkan",
        dataIndex: "kurspaverkan",
        key: "påverkan",
        render: text => {
            const colorMap = {
                låg: "default",
                mellan: "blue",
                hög: "orange",
                gigantisk: "red"
            };
            return <Tag color={colorMap[text] || "default"}>{text.toUpperCase()}</Tag>;
        }
    },
    {
        title: "Datum",
        dataIndex: "trigger_datum",
        key: "datum",
        render: text => <span style={{ whiteSpace: 'nowrap' }}>{text}</span>
    },
    {
        title: "Länk",
        dataIndex: "trigger_referens",
        key: "länk",
        render: (url) => <a href={url} target="_blank" rel="noreferrer">Länk</a>
    }
];

export default function TriggerTable() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:7000/api/triggers/")
            .then(res => setData(res.data))
            .catch(err => console.error(err));
    }, []);

    return <Table
        columns={columns}
        dataSource={data}
        pagination={false}
        rowKey="id"
    />;
}
