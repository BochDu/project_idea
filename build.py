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
    original_dir = os.getcwd()
    try:
        os.chdir(build_dir)
        # 使用make命令进行构建
        result = subprocess.run(['make'], check=True, capture_output=True, text=True, encoding='utf-8')
        print("Build output:")
        print(result.stdout)
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

# 主函数
def main():
    if clean_build_directory():
        if run_cmake():
            build_project()

if __name__ == "__main__":
    main()
