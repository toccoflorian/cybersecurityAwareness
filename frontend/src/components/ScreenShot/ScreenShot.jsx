import { useContext } from "react"
import { APIContext } from "../../APIServices/APIContext"



export default function ScreenShot() {

    const { fetchData, responseServer } = useContext(APIContext);

    async function handleClick() {
        fetchData('screenshot', null, "json")
        console.log(await responseServer);

    }




    return (<>
        <div className={`button-container`}>
            <p>Prendre une capture d&#39;écran</p>
            <button onClick={handleClick} className={`btn`}>Prendre une capture d&#39;écran</button>

        </div>
    </>)
}