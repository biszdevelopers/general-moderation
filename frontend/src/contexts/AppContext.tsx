import { createContext, useContext, useEffect, useState, ReactNode, ReactElement } from "react";
import { AuditService } from "../services/AuditService";
import { AuthService } from "../services/AuthService";
import { ExportService } from "../services/ExportService";
import { ModelManagementService } from "../services/ModelManagementService";
import { PhraseService } from "../services/PhraseService";
import { SemanticIndexService } from "../services/SemanticIndexService";
import { SettingsService } from "../services/SettingsService";
import { TestApiService } from "../services/TestApiService";
import { WordBankService } from "../services/WordBankService";

export interface AppContextType {
  authService: AuthService;
  wordBankService: WordBankService;
  auditService: AuditService;
  settingsService: SettingsService;
  exportService: ExportService;
  testApiService: TestApiService;
  phraseService: PhraseService;
  semanticIndexService: SemanticIndexService;
  modelService: ModelManagementService;
  authenticated: boolean;
  login: (key: string) => void;
  logout: () => void;
}

const apiBaseUrl: string = (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? "";

const AppContext = createContext<AppContextType | null>(null);

export function AppProvider(props: { children: ReactNode }): ReactElement {
  const [services] = useState(() => {
    const authService: AuthService = new AuthService(apiBaseUrl);
    return {
      authService,
      wordBankService: new WordBankService(authService, apiBaseUrl),
      auditService: new AuditService(authService, apiBaseUrl),
      settingsService: new SettingsService(authService, apiBaseUrl),
      exportService: new ExportService(authService, apiBaseUrl),
      testApiService: new TestApiService(authService, apiBaseUrl),
      phraseService: new PhraseService(authService, apiBaseUrl),
      semanticIndexService: new SemanticIndexService(authService, apiBaseUrl),
      modelService: new ModelManagementService(authService, apiBaseUrl),
    };
  });
  const [authenticated, setAuthenticated] = useState<boolean>(
    services.authService.isAuthenticated(),
  );

  useEffect(() => {
    return services.authService.onUnauthorized(() => setAuthenticated(false));
  }, [services]);

  const login = (key: string): void => {
    services.authService.setApiKey(key);
    setAuthenticated(true);
  };

  const logout = (): void => {
    services.authService.clearApiKey();
    setAuthenticated(false);
  };

  return (
    <AppContext.Provider
      value={{
        ...services,
        authenticated,
        login,
        logout,
      }}
    >
      {props.children}
    </AppContext.Provider>
  );
}

export function useAppContext(): AppContextType {
  const context: AppContextType | null = useContext(AppContext);
  if (context === null) {
    throw new Error("useAppContext must be used within an AppProvider");
  }
  return context;
}
