import { createContext, useContext, useEffect, useState, ReactNode, ReactElement } from "react";

const STORAGE_KEY: string = "moderation_admin_theme";

export interface ThemeContextType {
    dark: boolean;
    toggleDark: () => void;
}

const ThemeContext = createContext<ThemeContextType | null>(null);

export function ThemeProvider(props: { children: ReactNode }): ReactElement {
    const [dark, setDark] = useState<boolean>(() => localStorage.getItem(STORAGE_KEY) === "dark");

    useEffect(() => {
        document.documentElement.dataset.theme = dark ? "dark" : "light";
        localStorage.setItem(STORAGE_KEY, dark ? "dark" : "light");
    }, [dark]);

    const toggleDark = (): void => setDark((current) => !current);

    return (
        <ThemeContext.Provider value={{ dark, toggleDark }}>{props.children}</ThemeContext.Provider>
    );
}

export function useTheme(): ThemeContextType {
    const context: ThemeContextType | null = useContext(ThemeContext);
    if (context === null) {
        throw new Error("useTheme must be used within a ThemeProvider");
    }
    return context;
}
