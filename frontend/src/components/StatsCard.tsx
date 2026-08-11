import { Card, Statistic } from "antd";
import { ReactElement } from "react";

export interface StatsCardProps {
    title: string;
    value: number | string;
    suffix?: string;
}

export function StatsCard(props: StatsCardProps): ReactElement {
    return (
        <Card className="stats-card" variant="borderless">
            <Statistic title={props.title} value={props.value} suffix={props.suffix} />
        </Card>
    );
}
