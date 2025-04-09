import os
import shutil
import subprocess

# 定义项目根目录和build目录
project_root = '.'
build_dir = os.path.join(project_root, 'build')

# 步骤1: 删除build目录下的所有文件和文件夹
def clean_build_directory():
    try:
        if os.path.exists(build_dir):
            for root, dirs, files in os.walk(build_dir, topdown=False):
                for name in files:
                    file_path = os.path.join(root, name)
                    os.remove(file_path)
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    shutil.rmtree(dir_path)
            print("Build directory cleaned successfully.")
        else:
            print("Build directory does not exist.")
    except Exception as e:
        print(f"Error cleaning build directory: {e}")
        return False
    return True

# 步骤2: 执行cmake ..命令
def run_cmake():
    original_dir = os.getcwd()
    try:
        os.chdir(build_dir)
        result = subprocess.run(['cmake', '..'], check=True, capture_output=True, text=True, encoding='utf-8')
        print("CMake output:")
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"CMake failed: {e}")
        print("CMake error output:")
        print(e.stderr)
        return False
    finally:
        os.chdir(original_dir)

# 步骤3: 执行构建命令
def build_project():
    # 指定msbuild的完整路径
    msbuild_path = r'C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\amd64\MSBuild.exe'
    original_dir = os.getcwd()
    try:
        os.chdir(build_dir)
        # 使用Popen来非阻塞地运行msbuild
        process = subprocess.Popen([msbuild_path, 'ALL_BUILD.vcxproj'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, [msbuild_path, 'ALL_BUILD.vcxproj'], output=stdout, stderr=stderr)
        print("Build output:")
        print(stdout)
        # 打印Debug目录下的文件列表，检查可执行文件是否生成
        debug_dir = os.path.join(build_dir, 'Debug')
        if os.path.exists(debug_dir):
            print(f"Files in {debug_dir}:")
            for file in os.listdir(debug_dir):
                print(file)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print("Build error output:")
        print(e.stderr)
        return False
    finally:
        os.chdir(original_dir)

# 步骤4: 检查可执行文件是否存在
def run_executable():
    executable_name = 'chitu'
    executable_path = os.path.join(build_dir, 'Debug', f'{executable_name}.exe')
    print(f"Checking executable path: {executable_path}")
    # 再次检查Debug目录是否存在
    debug_dir = os.path.join(build_dir, 'Debug')
    print(f"Debug directory path: {debug_dir}")
    if not os.path.exists(debug_dir):
        print(f"Debug directory {debug_dir} not found.")
    if os.path.exists(executable_path):
        print(f"Executable {executable_path} found.")
    else:
        print(f"Executable {executable_path} not found.")

# 主函数
def main():
    if clean_build_directory():
        if run_cmake():
            if build_project():
                run_executable()

if __name__ == "__main__":
    main()
