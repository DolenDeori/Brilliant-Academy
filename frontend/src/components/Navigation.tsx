import { useState } from "react";
import { Bars3Icon, XMarkIcon } from "@heroicons/react/16/solid";
import { Dialog, DialogPanel } from "@headlessui/react";
import { navigation } from "../constant";
import { ChevronRightIcon } from "@heroicons/react/24/outline";

const Navigation = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  return (
    <div className="bg-white font-funnel">
      <header className="absolute inset-x-0 top-0 z-50">
        {/* --------- Navigation Start ----------- */}
        <nav
          aria-label="Global"
          className="flex items-center justify-between px-4 py-4 lg:py-0 lg:px-8 bg-white"
        >
          <div className="flex lg:flex-1">
            <a href="#" className="-m-1.5 p-1.5 text-xl">
              <span className="text-yellow-400 font-funnel-semi-bold">
                Brilliant
              </span>
              Academy
            </a>
          </div>

          {/* Hamberger Manue */}
          <div className="flex lg:hidden">
            <button
              type="button"
              onClick={() => setMobileMenuOpen(true)}
              className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
            >
              <span className="sr-only">Open main menu</span>
              <Bars3Icon aria-hidden="true" className="size-6" />
            </button>
          </div>
          <div className="hidden lg:flex lg:gap-x-6">
            {navigation.map((item) => (
              <a
                key={item.name}
                href={item.href}
                className={`text-sm/6 py-4 ${
                  item.active ? "text-red-400" : "text-gray-500"
                } block border-b-3 ${
                  item.active ? "" : "border-transparent"
                } py-2 ${
                  item.active ? "hover:border-red-400" : "hover:border-gray-600"
                } ${
                  item.active ? "hover:text-red-400" : "hover:text-gray-800"
                } duration-150`}
              >
                {item.name}
              </a>
            ))}
          </div>
          <div className="hidden lg:flex lg:flex-1 lg:justify-end">
            <a
              href="#"
              className="text-sm/6 font-funnel-medium border-2 p-1 px-4.5 border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white duration-200 flex justify-center items-center gap-2 rounded-full"
            >
              Register/Log in <ChevronRightIcon className="h-5 w-5 " />
            </a>
          </div>
        </nav>
        {/* ---------- Navigation End ----------------- */}

        {/* ------------ Mobile Navigation -------------- */}
        <Dialog
          open={mobileMenuOpen}
          onClose={setMobileMenuOpen}
          className="lg:hidden"
        >
          <div className="fixed inset-0 z-50" />
          <DialogPanel className="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
            <div className="flex items-center justify-between">
              <a href="#" className="-m-1.5 p-1.5 text-xl">
                <span className="text-yellow-400 font-funnel-semi-bold">
                  Brilliant
                </span>
                Academy
              </a>
              <button
                type="button"
                onClick={() => setMobileMenuOpen(false)}
                className="-m-2.5 rounded-md p-2.5 text-gray-700"
              >
                <span className="sr-only">Close menu</span>
                <XMarkIcon aria-hidden="true" className="size-6" />
              </button>
            </div>
            <div className="mt-6 flow-root">
              <div className="-my-6 divide-y divide-gray-500/10">
                <div className="space-y-2 py-6">
                  {navigation.map((item) => (
                    <a
                      key={item.name}
                      href={item.href}
                      className={`-mx-3 block rounded-lg px-3 py-2 text-base/7 ${
                        item.active ? "text-red-400" : "text-gray-900"
                      }  hover:bg-gray-50 font-funnel`}
                    >
                      {item.name}
                    </a>
                  ))}
                </div>
                <div className="py-6">
                  <a
                    href="#"
                    className="text-sm/6 border-2 p-1 px-4 border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white duration-200 flex justify-center items-center gap-2 font-funnel-medium rounded-full"
                  >
                    Register/Log in <ChevronRightIcon className="h-5 w-5" />
                  </a>
                </div>
              </div>
            </div>
          </DialogPanel>
        </Dialog>
        {/* ------------ Mobile Navigation -------------- */}
      </header>
    </div>
  );
};

export default Navigation;
