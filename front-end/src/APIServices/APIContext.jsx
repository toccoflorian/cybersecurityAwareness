import { createContext, useState } from "react";


export const APIContext = createContext();

export function DataProvider({ children }) {

    const [responseServer, setResponseServeur] = useState("Bienvenue, connectez vous pour démmarer.");
    const [displayContent, setDisplayContent] = useState(["Bienvenue, connectez vous pour démmarer."]);

    async function fetchData(endpoint = null, content, returnContentType = null) {


        let url = "http://localhost:12000/";
        endpoint && (url = url + endpoint)
        console.log(url);
        const response = await fetch(url, {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: content,
        })

        switch (returnContentType) {
            case "json":
                // console.log(response.json());

                setDisplayContent([await response.json()]);
                break;
            case "byte":
                setDisplayContent([...displayContent, response.body]);
                break;

            default:
                setDisplayContent([await response.text()]);
                break;
        }
    }

    return (<>
        <APIContext.Provider value={{ displayContent, fetchData }}>
            {children}
        </APIContext.Provider>
    </>)
}

