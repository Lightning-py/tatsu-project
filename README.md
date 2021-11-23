# AlTeX

Язык с упрощённым синтаксисом и структурой <img src="https://latex.codecogs.com/svg.latex?\fn_phv&space;LaTeX" title="LaTeX" />, транслируемый в код <img src="https://latex.codecogs.com/svg.latex?\fn_phv&space;LaTeX" title="LaTeX" />.

---

## ToDo

* [x] Базовые символы
* [x] Арифметические выражения
* [ ] Сумма / Произведение / Пределы
* [ ] Подстрочные / Надстрочные символы
* [ ] Блоки
  * [ ] Матрицы
  * [ ] СЛАУ

## Пример

Следующий код <img src="https://latex.codecogs.com/svg.latex?\fn_phv&space;\large&space;AlTeX" title="\large AlTeX" />

```
((alpha * 2) - 33) / 16 + beta - delta**2
```

транслируется в валиидный код <img src="https://latex.codecogs.com/svg.latex?\fn_phv&space;LaTeX" title="LaTeX" />

```latex
((\frac{(\alpha 2 - 33)}{16} + \beta) - \delta ^ 2)
```

и отобразится как:

<img src="https://latex.codecogs.com/svg.latex?\fn_phv&space;((\frac{(\alpha&space;2&space;-&space;33)}{16}&space;&plus;&space;\beta)&space;-&space;\delta&space;^&space;2)" title="((\frac{(\alpha 2 - 33)}{16} + \beta) - \delta ^ 2)" />
