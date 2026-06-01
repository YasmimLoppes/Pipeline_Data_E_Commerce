# ⚖️ DOCUMENTAÇÃO: REGRAS DE NEGÓCIO E QUALIDADE DE DADOS

Todas as regras aplicadas neste projeto foram definidas com base na experiência prática com Controle de Estoque e Operação de Caixa.

---

## ✅ REGRA 1: DADO BRUTO É IMUTÁVEL
Os arquivos dentro da pasta `raw` NUNCA são alterados. Igual a uma Nota Fiscal original: pode conferir, mas não mudar.

## ✅ REGRA 2: NÃO EXISTEM DADOS DUPLICADOS
Remoção de duplicatas pela chave `id` para evitar contagem errada do estoque.

## ✅ REGRA 3: CAMPOS OBRIGATÓRIOS SÃO INEGOCIÁVEIS
Sem `id`, `nome`, `preço` ou `categoria`, o registro é descartado. Dado incompleto é dado inútil.

## ✅ REGRA 4: VALORES NUMÉRICOS DEVEM SER LÓGICOS
Preço deve ser > R$ 0,01 e < R$ 10.000,00. Não aceita texto nem valor negativo.

## ✅ REGRA 5: PADRONIZAÇÃO DE TEXTO
Categorias e nomes são formatados para evitar que "Celular" e "celular" sejam vistos como coisas diferentes.

## ✅ REGRA 6: CÁLCULOS DE VALOR AGREGADO
Transformamos preço unitário em informações de lucro e valor total de estoque.

## ✅ REGRA 7: RASTREABILIDADE TOTAL
Todo dado tratado carrega a data de processamento e a origem. Essencial para auditoria.