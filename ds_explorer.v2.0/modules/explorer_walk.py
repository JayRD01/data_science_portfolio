import os
from modules.abstracted import AbstractedClass


class ExplorerLight(AbstractedClass):
    def explorer_walk(self):
        # Count how many separators the root path has — used to calculate depth during walk
        root_depth_count = self.root_path.rstrip(os.sep).count(os.sep)

        try:
            for dirpath, dirnames, filenames in os.walk(self.root_path, followlinks=False):
                # Calculate current depth relative to the root
                current_depth = dirpath.count(os.sep) - root_depth_count

                # Skip subdirectories if depth limit has been reached
                if self.max_depth != -1 and current_depth >= self.max_depth:
                    dirnames.clear()  # Clear prevents os.walk from descending further
                    continue

                # Process subdirectories
                for dirname in dirnames:
                    try:
                        full_path = os.path.join(dirpath, dirname)
                        self.visited_dir.add(full_path)
                    except Exception as e:
                        print(f"Error adding directory '{dirname}': {e}")

                # Process files
                for filename in filenames:
                    try:
                        file_path = os.path.join(dirpath, filename)
                        self.filenames.add(file_path)
                    except Exception as e:
                        print(f"Error adding file '{filename}': {e}")

        except PermissionError:
            print(f"Permission denied while walking: {self.root_path}")
        except FileNotFoundError:
            print(f"Starting path not found: {self.root_path}")
        except Exception as e:
            print(f"Unexpected error during walk: {e}")

        # Return the collected results
        return self.visited_dir, self.filenames

    def run(self):
        """
        Implements the abstract 'run' method.
        Executes the walk-based exploration and returns the results.
        """
        return self.explorer_walk()


""" 
Gestión de Archivos:

Leer y escribir archivos usando rutas generadas por os.path.
Renombrar y mover archivos entre carpetas.
Crear y eliminar archivos temporales.
Gestión de Directorios:

Crear, renombrar y eliminar directorios.
Comprobar permisos de lectura, escritura y ejecución.
Detectar directorios vacíos.
Metadatos de Archivos:

Obtener tamaño, fecha de creación, última modificación y permisos con os.stat.
Convertir timestamps a formatos legibles por humanos.
Permisos y Propiedades del Sistema:

Comprobar y establecer permisos con os.chmod.
Cambiar propietarios y grupos (si es aplicable en tu sistema operativo).
Determinar el sistema operativo en uso (os.name o os.uname).
Variables de Entorno:

Leer variables de entorno con os.environ.
Añadir, modificar o eliminar variables temporales.
Manipulación de Rutas:

Unir, dividir y normalizar rutas con os.path.
Detectar rutas absolutas o relativas.
Obtener nombres de archivos o extensiones.
Ejecutar Comandos del Sistema:

Ejecutar comandos de shell con os.system.
Capturar salidas o errores del sistema.
Procesos y Señales:

Iniciar procesos secundarios con os.fork (si está disponible).
Enviar señales a procesos en ejecución (os.kill).
Automatización de Tareas del Sistema:

Realizar copias de seguridad automáticas.
Crear scripts de limpieza que eliminen archivos duplicados o no utilizados.
Registrar los cambios en archivos y directorios en tiempo real.

"""
