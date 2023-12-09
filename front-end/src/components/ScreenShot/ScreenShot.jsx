import { useContext } from "react"
import { APIContext } from "../../APIServices/APIContext"



export default function ScreenShot() {

    const { fetchData, responseServer } = useContext(APIContext);

    async function handleClick() {
        fetchData(null, "salut")
        console.log(await responseServer);

    }




    return (<>
        <div>
            <button onClick={handleClick} className={`btn`}>Prendre une capture d&#39;écran</button>

        </div>
    </>)
}