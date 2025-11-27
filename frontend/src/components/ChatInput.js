import React, { useState } from "react";

export default function ChatInput({ onSend }) {
    const [text, setText] = useState("");

    function submit() {
        if (!text.trim()) return;
        onSend(text.trim());
        setText("");
    }

    return (
        <>
            <input
                type="text"
                value={text}
                placeholder="Enter your query..."
                onChange={e => setText(e.target.value)}
                onKeyDown={e => e.key === "Enter" && submit()}
            />
            <button onClick={submit}>Send</button>
        </>
    );
}
