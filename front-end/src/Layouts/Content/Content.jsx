import Display from "../../components/Display/Display";
import ButtonBar from "../ButtonBar/ButtonBar";


export default function Content() {

    return (<>
        <div className={`width90 mlr-auto `}>
            <ButtonBar />
            <Display />
        </div>

    </>)
}