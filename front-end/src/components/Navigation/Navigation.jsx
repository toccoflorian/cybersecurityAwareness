import { useContext, useEffect, useState } from "react";
import { APIContext } from "../../APIServices/APIContext"

export default function Navigation() {

    const { fetchData, displayContent } = useContext(APIContext);
    const [inputContent, setInputContent] = useState("");

    function handleGoDir() {
        fetchData("go_dir", inputContent, "json")
    }

    function handleBack() {
        fetchData('go_back', null, "json")
    }


    return (<>
        <div className={`d-flex flex-column`}>

            <p>Elements ne se terminant pas par &#34;@&#34;.</p>

            <div className={`mb10`}>

                <input onChange={(e) => setInputContent(e.target.value)} type="text" />
                <button onClick={handleGoDir}>Aller</button>
            </div>
            <button onClick={() => fetchData("get_current_dir", null, "json")}>Voir</button>
            <button onClick={handleBack} className={`btn`}>précedent</button>

        </div>
    </>)
}