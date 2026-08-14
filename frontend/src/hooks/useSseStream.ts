import { useCallback, useState } from "react";
import { StreamEvent } from "../types";

export interface UseSseStreamResult {
    running: boolean;
    events: StreamEvent[];
    error: string | null;
    start: (
        producer: (onEvent: (event: StreamEvent) => void) => Promise<unknown>,
    ) => Promise<unknown>;
    reset: () => void;
}

export function useSseStream(): UseSseStreamResult {
    const [running, setRunning] = useState<boolean>(false);
    const [events, setEvents] = useState<StreamEvent[]>([]);
    const [error, setError] = useState<string | null>(null);

    const start = useCallback(
        async (producer: (onEvent: (event: StreamEvent) => void) => Promise<unknown>) => {
            setRunning(true);
            setError(null);
            setEvents([]);
            try {
                return await producer((event) => {
                    setEvents((current) => [...current, event]);
                });
            } catch (err: unknown) {
                setError(String(err));
                return null;
            } finally {
                setRunning(false);
            }
        },
        [],
    );

    const reset = useCallback((): void => {
        setEvents([]);
        setError(null);
    }, []);

    return { running, events, error, start, reset };
}
