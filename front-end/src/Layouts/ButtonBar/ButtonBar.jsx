import Destruction from "../../components/Destruction/Destruction";
import Download from "../../components/Download/Download";
import Execute from "../../components/Execute/Execute";
import Navigation from "../../components/Navigation/Navigation";
import ScreenShot from "../../components/ScreenShot/ScreenShot";

import styles from "./ButtonBar.module.scss";



export default function ButtonBar() {

    return (<>
        <div className={`${styles.buttonBarContainer} d-flex flex-wrap justify-space-e align-center debuggreen`}>
            <Navigation />
            <Download />
            <Execute />
            <ScreenShot />
            <Destruction />
        </div>
    </>)
}