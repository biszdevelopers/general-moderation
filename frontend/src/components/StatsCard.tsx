import { Card } from "antd";
import { ReactElement } from "react";

export interface StatsCardProps {
    title: string;
    value: number | string;
    suffix?: string;
    icon?: ReactElement;
    color?: string;
}

export function StatsCard(props: StatsCardProps): ReactElement {
    const { title, value, suffix, icon, color = "#2563eb" } = props;
    return (
        <Card className="stats-card" variant="borderless">
            <div className="stats-card__inner">
                {icon !== undefined && (
                    <div className="stats-card__icon" style={{ background: `${color}1a`, color }}>
                        {icon}
                    </div>
                )}
                <div>
                    <div className="stats-card__title">{title}</div>
                    <div className="stats-card__value">
                        {value}
                        {suffix !== undefined && (
                            <span className="stats-card__suffix">{suffix}</span>
                        )}
                    </div>
                </div>
            </div>
        </Card>
    );
}
