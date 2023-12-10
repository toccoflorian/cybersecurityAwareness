import { useContext, useEffect, useState } from "react";
import { APIContext } from "../../APIServices/APIContext"

export default function Navigation() {

    const { fetchData, responseServer } = useContext(APIContext);
    const [currentDir, setCurrentDir] = useState([]);


    async function handleFocus() {
        fetchData('navigate', "dir")
        console.log(await responseServer);
        setCurrentDir(await responseServer.split(" -%- "))
    }

    function handleChange(e) {

        fetchData("navigate", "cd " + e.target.value)
        // setTimeout(() => { }, 1000)


    }

    function handleBack() {
        fetchData('navigate', "cd ..")


    }


    return (<>
        <div className={`d-flex flex-column`}>

            <div className={`mb10`}>

                {/* <button className={`btn`}>aller dans</button> */}
                <select onChange={handleChange} onFocus={handleFocus} defaultValue="" placeholder="Aller dans le répertoire">
                    <option disabled value="">Aller dans le répertoire</option>
                    {currentDir.map((element, i) => <option key={i} value={element}>{element}</option>)}

                </select>
            </div>

            <button onClick={handleBack} className={`btn`}>précedent</button>

        </div>
    </>)
}