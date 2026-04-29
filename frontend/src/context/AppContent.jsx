import { createContext, useState } from "react";

export const AppContext = createContext();

export default function AppProvider({ children }) {
  const [result, setResult] = useState(null);

  return (
    <AppContext.Provider value={{ result, setResult }}>
      {children}
    </AppContext.Provider>
  );
}