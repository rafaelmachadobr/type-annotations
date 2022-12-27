# Type Annotations

Este repositório contém exemplos de utilização de anotações de tipo em Python. As anotações de tipo são uma forma de adicionar informações de tipo aos códigos Python, permitindo que ferramentas como o Mypy possam realizar verificações de tipo estático.

## Arquivos
- **"annotations.py"**: contém exemplos de anotações de tipo em diversos contextos, como em funções, métodos e atributos de classe.
- **"typing.py"**: mostra como utilizar o módulo **"typing"** para criar anotações de tipo mais complexas, como tipos genéricos e conjuntos de tipos.
- **"exceptions.py"**: demonstra como anotar exceções lançadas por uma função.

## Utilização
Para utilizar as anotações de tipo nestes exemplos, é necessário ter o Mypy instalado. Ele pode ser instalado com o seguinte comando:

```pip install mypy```

Em seguida, basta rodar o Mypy passando o nome do arquivo como parâmetro para verificar as anotações de tipo:

```mypy annotations.py```

O Mypy irá verificar se os tipos estão sendo utilizados corretamente e apontar possíveis erros de tipagem.
