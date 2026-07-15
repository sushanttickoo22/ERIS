const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("eris", {
    version: "0.1.0"
});
