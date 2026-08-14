import { ReactElement } from "react";
import { Tooltip } from "antd";

export interface BarDatum {
    label: string;
    value: number;
    hint?: string;
    color?: string;
}

export function BarChart(props: { data: BarDatum[]; height?: number }): ReactElement {
    const { data, height = 140 } = props;
    const max: number = Math.max(1, ...data.map((item) => item.value));
    return (
        <div className="bar-chart" style={{ height }}>
            {data.map((item) => (
                <Tooltip key={item.label} title={item.hint ?? `${item.label}: ${item.value}`}>
                    <div className="bar-chart__col">
                        <div
                            className="bar-chart__bar"
                            style={{
                                height: `${Math.max(2, (item.value / max) * 88)}%`,
                                backgroundColor: item.color ?? "#2563eb",
                            }}
                        />
                        <div className="bar-chart__label">{item.label}</div>
                    </div>
                </Tooltip>
            ))}
        </div>
    );
}
