import { ReactElement, useEffect, useRef } from "react";
import { Card, Empty, Space, Tag, Typography } from "antd";
import { SyncOutlined } from "@ant-design/icons";
import { StreamEvent } from "../../types";

function eventColor(name: string): string {
    if (name === "complete") {
        return "green";
    }
    if (name === "error") {
        return "red";
    }
    if (name === "stage1_complete" || name === "stage2_complete" || name === "stage3_complete") {
        return "blue";
    }
    if (name === "detector_result") {
        return "purple";
    }
    if (name === "progress") {
        return "cyan";
    }
    return "default";
}

export function LiveStreamPanel(props: { events: StreamEvent[]; running: boolean }): ReactElement {
    const { events, running } = props;
    const containerRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        if (containerRef.current !== null) {
            containerRef.current.scrollTop = containerRef.current.scrollHeight;
        }
    }, [events]);

    const extra: ReactElement = running ? (
        <Space size="small">
            <SyncOutlined spin />
            <Typography.Text type="secondary">streaming</Typography.Text>
        </Space>
    ) : (
        <Typography.Text type="secondary">
            {events.length} event{events.length === 1 ? "" : "s"}
        </Typography.Text>
    );

    return (
        <Card title="Live Stream" className="workbench-card" extra={extra}>
            {events.length === 0 ? (
                <Empty description="Press Moderate above to stream the pipeline events in real time." />
            ) : (
                <div className="live-stream" ref={containerRef}>
                    {events.map((event, index) => (
                        <div className="live-stream__frame" key={`${event.name}-${index}`}>
                            <Space>
                                <Tag color={eventColor(event.name)}>{event.name}</Tag>
                                <Typography.Text type="secondary">
                                    frame {index + 1}
                                </Typography.Text>
                            </Space>
                            <pre className="workbench-pre">
                                {JSON.stringify(event.data, null, 2)}
                            </pre>
                        </div>
                    ))}
                </div>
            )}
        </Card>
    );
}
