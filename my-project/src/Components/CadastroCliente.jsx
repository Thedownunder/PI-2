import React, { useState } from "react";
import NavBar from "./NavBar";
// import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css"; // Importa o estilo do DatePicker
import InputMask from 'react-input-mask';

export default function CadastroCliente() {
  const [dataNascimento, setDataNascimento] = useState(null);

  return (
    <>
      <div>
        <NavBar />
      </div>
      <div className="flex items-center justify-center py-10">
        <form>
          <div className="min-h-full flex-1 flex-col justify-center border-b border-gray-900/10 pb-12">
            <h2 className="text-base/7 font-semibold text-gray-900">Cadastro do Cliente</h2>
            <p className="mt-1 text-sm/6 text-gray-600">Insira abaixo as informações do cliente</p>

            <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-3">
                <label htmlFor="first-name" className="block text-sm/6 font-medium text-gray-900">Nome</label>
                <div className="mt-2">
                  <input type="text" name="first-name" id="first-name" autoComplete="given-name" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="last-name" className="block text-sm/6 font-medium text-gray-900">Sobrenome</label>
                <div className="mt-2">
                  <input type="text" name="last-name" id="last-name" autoComplete="family-name" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-4">
                <label htmlFor="email" className="block text-sm/6 font-medium text-gray-900">Email</label>
                <div className="mt-2">
                  <input id="email" name="email" type="email" autoComplete="email" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="telefone" className="block text-sm/6 font-medium text-gray-900">Telefone</label>
                <div className="mt-2">
                  <InputMask
                    type="text"
                    mask="+55 (99) 99999-9999"
                    maskChar=""
                    name="telefone"
                    id="telefone"
                    autoComplete="tel"
                    className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"
                  />
                  {/* <input type="text" name="telefone" id="telefone" maxLength={11} placeholder="( )_____-____" autoComplete="given-telefone" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" /> */}
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="sexo" className="block text-sm/6 font-medium text-gray-900">Sexo</label>
                <div className="mt-2">
                  <select id="sexo" name="sexo" autoComplete="sexo" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm">
                    <option>Masculino</option>
                    <option>Feminino</option>
                    <option>Outro</option>
                  </select>
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="cpf" className="block text-sm/6 font-medium text-gray-900">CPF</label>
                <div className="mt-2">
                  <InputMask
                    type="text"
                    mask="999.999.999-99"
                    maskChar=""
                    name="cpf"
                    id="cpf"
                    autoComplete="cpf"
                    className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"
                  />
                  {/* <input type="text" name="cpf" id="cpf" maxLength={11} autoComplete="cpf" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" /> */}
                </div>
              </div>

              <div className="sm:col-span-3">
                <label htmlFor="data-nasc" className="block text-sm/6 font-medium text-gray-900">Data de nascimento</label>
                <div className="mt-2">
                  <InputMask
                    type="text"
                    mask="99/99/9999"
                    maskChar=""
                    name="data-nasc"
                    id="data-nasc"
                    autoComplete="data-nasc"
                    className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"
                  />
                </div>
              </div>

              <div className="sm:col-span-2 sm:col-start-1">
                <label htmlFor="city" className="block text-sm/6 font-medium text-gray-900">Cidade</label>
                <div className="mt-2">
                  <input type="text" name="city" id="city" autoComplete="address-level2" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="region" className="block text-sm/6 font-medium text-gray-900">Estado</label>
                <div className="mt-2">
                  <input type="text" name="region" id="region" autoComplete="address-level1" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="postal-code" className="block text-sm/6 font-medium text-gray-900">CEP</label>
                <div className="mt-2">
                  <input type="text" name="postal-code" id="postal-code" autoComplete="postal-code" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"/>
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="street-address" className="block text-sm/6 font-medium text-gray-900">Complemento</label>
                <div className="mt-2">
                  <input type="text" name="street-address" id="street-address" autoComplete="street-address" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div className="mt-6 flex items-center justify-center gap-x-6">
        <button type="button" className="text-sm/6 font-semibold text-gray-900">Cancel</button>
        <button type="submit" className="rounded-md bg-orange-800 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
      </div>
    </>
  );
}
