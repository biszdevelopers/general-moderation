import { beforeEach, describe, expect, it } from "vitest";
import { AuthService } from "./AuthService";

describe("AuthService", () => {
    beforeEach(() => {
        localStorage.clear();
    });

    it("starts unauthenticated without a stored key", () => {
        const service: AuthService = new AuthService("");
        expect(service.isAuthenticated()).toBe(false);
        expect(service.headers()).toEqual({ "Content-Type": "application/json" });
    });

    it("persists the key and authenticates", () => {
        const service: AuthService = new AuthService("");
        service.setApiKey("secret-key");
        expect(service.isAuthenticated()).toBe(true);
        expect(service.headers()["X-API-Key"]).toBe("secret-key");
        expect(localStorage.getItem("moderation_admin_api_key")).toBe("secret-key");
        expect(new AuthService("").isAuthenticated()).toBe(true);
    });

    it("clears the key on logout", () => {
        const service: AuthService = new AuthService("");
        service.setApiKey("secret-key");
        service.clearApiKey();
        expect(service.isAuthenticated()).toBe(false);
        expect(localStorage.getItem("moderation_admin_api_key")).toBeNull();
    });

    it("clears the key and notifies handlers on unauthorized", () => {
        const service: AuthService = new AuthService("");
        service.setApiKey("bad-key");
        const notified: number[] = [];
        service.onUnauthorized(() => notified.push(1));
        service.handleUnauthorized();
        expect(notified).toEqual([1]);
        expect(service.isAuthenticated()).toBe(false);
    });

    it("unsubscribes unauthorized handlers", () => {
        const service: AuthService = new AuthService("");
        service.setApiKey("key");
        const notified: number[] = [];
        const unsubscribe: () => void = service.onUnauthorized(() => notified.push(1));
        unsubscribe();
        service.handleUnauthorized();
        expect(notified).toEqual([]);
        expect(service.isAuthenticated()).toBe(false);
    });
});
