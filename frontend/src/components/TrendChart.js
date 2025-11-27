import React from "react";
import {
    LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend,
    ResponsiveContainer
} from "recharts";

export default function TrendChart({ data }) {
    if (!data || data.length === 0) return null;

    return (
        <div style={{ width: "100%", height: 280 }}>
            <ResponsiveContainer>
                <LineChart data={data}>
                    <CartesianGrid stroke="#333" />
                    <XAxis dataKey="year" stroke="#ccc" />
                    <YAxis stroke="#ccc" />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="price" stroke="#00b3ff" strokeWidth={2} />
                    <Line type="monotone" dataKey="demand" stroke="#00ff8a" strokeWidth={2} />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
}
