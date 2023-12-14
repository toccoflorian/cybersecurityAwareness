
import { useState } from "react"
import { DataProvider } from "./APIServices/APIContext"
import "./App.scss"

import Header from "./components/Header/Header"
import Content from "./Layouts/Content/Content"




function App() {


  const [firstCommande, setfirstCommande] = useState(true)


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
