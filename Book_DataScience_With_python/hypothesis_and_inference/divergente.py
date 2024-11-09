import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Passo 1: Definir o grid 3D
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(-2, 2, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Passo 2: Definir o campo vetorial F = (x, y, z)
U = X
V = Y
W = Z

# Passo 3: Calcular a divergência: div(F) = dU/dx + dV/dy + dW/dz
# Aqui, div(F) será constante e igual a 3 em todos os pontos
div_F = np.ones_like(X) * 3

# Passo 4: Visualizar em 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotando o campo vetorial
ax.quiver(X, Y, Z, U, V, W, length=0.1, normalize=True, color='b')

# Plotando a divergência como um scatter plot
# Usamos a cor para representar a magnitude da divergência
img = ax.scatter(X, Y, Z, c=div_F, cmap='coolwarm', s=20)

# Adicionando a barra de cores para mostrar a escala de divergência
cbar = fig.colorbar(img)
cbar.set_label('Divergence')

# Configurações adicionais de plotagem
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Field and Divergence')

plt.show()
