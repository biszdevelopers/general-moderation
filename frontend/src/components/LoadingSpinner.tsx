import { Spin } from "antd";
import { ReactElement } from "react";

export function LoadingSpinner(): ReactElement {
    return (
        <div className="loading-spinner">
            <Spin size="large" />
        </div>
    );
}
