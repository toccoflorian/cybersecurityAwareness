
import "./App.scss"
import { createContext, useState } from "react"
import Header from "./components/Header/Header"
import Content from "./Layouts/Content/Content"

function App() {

  const tailleDisponibleContext = createContext(null);

  function DataProvider({ children }) {
    const [tailleDisponible, setTailleDisponible] = useState(null);
    const contextValue = { tailleDisponible, setTailleDisponible }

    return (<>
      <tailleDisponibleContext.Provider value={contextValue}>
        {children}
      </tailleDisponibleContext.Provider>
    </>)
  }

  return (
    <>
      <DataProvider>
        <Header />
        <Content />
      </DataProvider>

    </>
  )
}

export default App
