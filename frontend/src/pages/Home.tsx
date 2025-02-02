import { images } from "../constant";

const Home = () => {
  return (
    <main>
      <section className="h-svh w-full flex flex-col justify-center gap-2 items-center overflow-hidden relative">
        <div>
          <div className="font-funnel-medium text-center text-white">
            <p className="text-xl uppercase">Welcome To</p>
            <h1 className="text-6xl">Brilliant Academy</h1>
          </div>
        </div>
        <div className="h-[90svh] w-full bg-black absolute -z-2">
          <img
            src={images.header1}
            alt="banner image"
            className="absolute top-0 left-0 h-[90svh] w-full bg-cover -z-1 object-cover opacity-50"
          />
        </div>
        <div className="flex gap-x-4 mt-5">
          <button className="p-2 bg-blue-500 px-4 rounded-full font-funnel-medium text-white cursor-pointer">
            Appy Now
          </button>
          <button className="p-2 border-2 duration-300 hover:bg-blue-500 px-4 rounded-full font-funnel-medium text-white cursor-pointer">
            Register
          </button>
        </div>
      </section>
    </main>
  );
};

export default Home;
