export default function ListItem(props) {
  return (
    <li>
      <a target="_blank" href={props.url} rel="noreferrer">
        <img src={props.imageUrl} alt={props.alt} />
      </a>
    </li>
  );
}
