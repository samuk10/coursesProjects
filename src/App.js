import "./App.css";
import Header from "./components/Header";
import Section from "./components/Section";
import ListItem from "./components/ListItem";

const gamesListData = [
  {
    url: "https://www.twitch.tv/directory/game/counter-strike",
    imageUrl: "https://static-cdn.jtvnw.net/ttv-boxart/32399-144x192.jpg",
    alt: "Imagem do jogo Counter Strike",
  },

  {
    url: "https://www.twitch.tv/directory/game/world-of-warcraft",
    imageUrl: "https://static-cdn.jtvnw.net/ttv-boxart/18122-144x192.jpg",
    alt: "Imagem do jogo World of Warcraft",
  },

  {
    url: "https://www.twitch.tv/directory/category/throne-and-liberty",
    imageUrl: "https://static-cdn.jtvnw.net/ttv-boxart/19801_IGDB-144x192.jpg",
    alt: "Imagem do jogo Throne and Liberty",
  },

  {
    url: "https://www.twitch.tv/directory/game/tarisland",
    imageUrl:
      "https://static-cdn.jtvnw.net/ttv-boxart/1746026634_IGDB-144x192.jpg",
    alt: "Imagem do jogo Tarisland",
  },
];

const channelListData = [
  {
    url: "https://www.twitch.tv/samukarb",
    imageUrl:
      "https://static-cdn.jtvnw.net/jtv_user_pictures/samukarb-profile_image-eac00c2067be973a-70x70.png",
    alt: "Imagem de samukarb",
  },
  {
    url: "https://www.twitch.tv/vncsmoraiss",
    imageUrl:
      "https://static-cdn.jtvnw.net/jtv_user_pictures/0175eb09-dcd2-4940-91cc-fcd20b8c3dc0-profile_image-70x70.png",
    alt: "Imagem de vncsmoraiss",
  },
  {
    url: "https://www.twitch.tv/maykbrito",
    imageUrl:
      "https://static-cdn.jtvnw.net/jtv_user_pictures/9ce11a2b-ec84-44b1-9c76-b8d29df5fef0-profile_image-150x150.png",
    alt: "Imagem de Mayk Brito",
  },
  {
    url: "https://www.twitch.tv/alanzoka",
    imageUrl:
      "https://static-cdn.jtvnw.net/jtv_user_pictures/64d44235-1dee-4bca-95da-bee1ee96eea3-profile_image-70x70.png",
    alt: "Imagem de Alanzoka",
  },
  {
    url: "https://www.twitch.tv/cellbit",
    imageUrl:
      "https://static-cdn.jtvnw.net/jtv_user_pictures/0595cdd0-65a7-4fa3-996d-323cf3a54be1-profile_image-70x70.png",
    alt: "Imagemd de Cellbit",
  },
];

const socialListData = [
  {
    url: "https://www.twitch.com/samukarb",
    imageUrl: "/assets/twitch.svg",
    alt: "Imagem de Samukarb no Twitch",
  },
  {
    url: "https://www.instagram.com/samukarb",
    imageUrl: "/assets/instagram.svg",
    alt: "Imagem de Samukarb no Instagram",
  },
  {
    url: "https://www.twitter.com/samukarb",
    imageUrl: "/assets/twitter.svg",
    alt: "Imagem de Samukarb no Twitter",
  },
  {
    url: "https://www.youtube.com/samukarbrj",
    imageUrl: "/assets/youtube.svg",
    alt: "Imagem de Samukarb no Youtube",
  },
];

function App() {
  return (
    <div className="App">
      <Header />

      <main>
        <Section
          title="Meus Jogos"
          subtitle="Os games que eu mais curto jogar"
          className="games-list"
        >
          {gamesListData.map(function (item) {
            return (
              <ListItem
                url={item.url}
                imageUrl={item.imageUrl}
                alt={item.alt}
              />
            );
          })}
        </Section>
        <Section
          title="Canais e Streamers"
          subtitle="Lista de canais e transmissões que não perco"
          className="channel-list"
        >
          {channelListData.map(function (item) {
            return (
              <ListItem
                url={item.url}
                imageUrl={item.imageUrl}
                alt={item.alt}
              />
            );
          })}
        </Section>

        <Section
          title="Minhas Redes"
          subtitle="Se conecte comigo agora mesmo!"
          className="social-list"
        >
          {socialListData.map(function (item) {
            return (
              <ListItem
                url={item.url}
                imageUrl={item.imageUrl}
                alt={item.alt}
              />
            );
          })}
        </Section>
      </main>
    </div>
  );
}

export default App;
