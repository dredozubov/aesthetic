Собственно проблема возникала, когда я хотел нарисовать какой-либо график:
  

.. code-block::octave

	>> t = [0:0.01:0.99];
	>> hist(sin(3*pi*t),t)
	gnuplot> set terminal aqua enhanced title "Figure 1"  font "*,6"
	                      ^
	         line 0: unknown or ambiguous terminal type; type just 'set terminal' ...

Лечится(при наличии установленного X11) добавлением в octaverc:

.. code-block::

	setenv("GNUTERM","X11")

А так можно поменять приглашение в REPL'e:

.. code-block::

    PS1(">> ")