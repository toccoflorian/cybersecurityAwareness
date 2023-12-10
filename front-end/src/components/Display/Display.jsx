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
            <ul>

                {Object.values(content)
                    .map((element, i) => <li key={i}><ul>{element
                        .split(" -%-")
                        .map((dos, j) => {
                            return <li key={j}>{dos}</li>
                        })}</ul></li>)}
            </ul>
        </div>

    </>)
}