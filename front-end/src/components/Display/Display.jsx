import { useContext, useEffect, useState } from "react";
import styles from "./Display.module.scss";
import { APIContext } from "../../APIServices/APIContext";

export default function Display() {

    const { responseServer, fetchData } = useContext(APIContext);
    const [content, setContent] = useState([]);
    useEffect(() => {
        setContent([...content, "    --------------------------", responseServer])

    }, [responseServer])

    return (<>

        <div className={`${styles.displayContainer} `}>
            {content.map((line, i) => <p key={i}>{line}</p>)}
        </div>

    </>)
}