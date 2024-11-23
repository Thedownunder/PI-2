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
              <div className="sm:col-span-6">
                <label htmlFor="name" className="block text-sm/6 font-medium text-gray-900">Nome Completo</label>
                <div className="mt-2">
                  <input type="text" name="name" id="name" autoComplete="given-name" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-3">
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

              <div className="sm:col-span-3">
                <label htmlFor="estado" className="block text-sm/6 font-medium text-gray-900">Estado</label>
                <div className="mt-2">
                  <select id="estado" name="estado" autoComplete="estado" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm">
                    <option value="" disabled selected>Selecione um estado</option>
                    <option value="AC">Acre</option>
                    <option value="AL">Alagoas</option>
                    <option value="AP">Amapá</option>
                    <option value="AM">Amazonas</option>
                    <option value="BA">Bahia</option>
                    <option value="CE">Ceará</option>
                    <option value="DF">Distrito Federal</option>
                    <option value="ES">Espírito Santo</option>
                    <option value="GO">Goiás</option>
                    <option value="MA">Maranhão</option>
                    <option value="MT">Mato Grosso</option>
                    <option value="MS">Mato Grosso do Sul</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="PA">Pará</option>
                    <option value="PB">Paraíba</option>
                    <option value="PR">Paraná</option>
                    <option value="PE">Pernambuco</option>
                    <option value="PI">Piauí</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="RN">Rio Grande do Norte</option>
                    <option value="RS">Rio Grande do Sul</option>
                    <option value="RO">Rondônia</option>
                    <option value="RR">Roraima</option>
                    <option value="SC">Santa Catarina</option>
                    <option value="SP">São Paulo</option>
                    <option value="SE">Sergipe</option>
                    <option value="TO">Tocantins</option>
                  </select>
                </div>
              </div>

              <div className="sm:col-span-2 sm:col-start-1">
                <label htmlFor="city" className="block text-sm/6 font-medium text-gray-900">Cidade</label>
                <div className="mt-2">
                  <input type="text" name="city" id="city" autoComplete="address-level2" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="postal-code" className="block text-sm/6 font-medium text-gray-900">CEP</label>
                <div className="mt-2">
                  <InputMask
                    type="text"
                    mask="99999-999"
                    maskChar=""
                    name="postal-code"
                    id="postal-code"
                    autoComplete="postal-code"
                    className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"
                  />
                  {/* <input type="text" name="postal-code" id="postal-code" autoComplete="postal-code" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm"/> */}
                </div>
              </div>

              <div className="sm:col-span-2">
                <label htmlFor="bairro" className="block text-sm/6 font-medium text-gray-900">Bairro</label>
                <div className="mt-2">
                  <input id="bairro" name="bairro" type="bairro" autoComplete="street" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="col-span-3">
                <label htmlFor="rua" className="block text-sm/6 font-medium text-gray-900">Rua</label>
                <div className="mt-2">
                  <input type="text" name="rua" id="rua" autoComplete="rua" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="col-span-3">
                <label htmlFor="numero" className="block text-sm/6 font-medium text-gray-900">Número</label>
                <div className="mt-2">
                  <input type="text" name="numero" id="numero" autoComplete="numero" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="street-address" className="block text-sm/6 font-medium text-gray-900">Endereço</label>
                <div className="mt-2">
                  <input type="text" name="street-address" id="street-address" autoComplete="street-address" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="complemento" className="block text-sm/6 font-medium text-gray-900">Complemento</label>
                <div className="mt-2">
                  <input type="text" name="complemento" id="complemento" autoComplete="complemento" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div className="mb-4 flex items-center justify-center gap-x-6">
        <button type="button" className="text-sm/6 font-semibold rounded-md px-3 py-2 hover:bg-yellow-900 hover:text-white text-gray-900">Cancelar</button>
        <button type="submit" className="rounded-md bg-orange-800 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-yellow-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Salvar</button>
      </div>
    </>
  );
}
