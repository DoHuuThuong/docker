import streamlit as st
from code_runner import run_code_in_docker
from test_cases import get_test_cases
from streamlit_monaco import st_monaco

language = st.selectbox("Select Language", ["Java", "C"])
print(language.lower())
content = st_monaco(
    value="// First line\nfunction hello() {\n\talert('Hello world!');\n}\n// Last line",
    height="200px",
    language=f'{language.lower()}',
    lineNumbers=True,
    minimap=False,
    theme="vs-dark",
)


    
# code = st.text_area("Write your code here")


if st.button("Run Code"):
    # st.markdown(f"```javascript{content}")
    test_cases = get_test_cases(language)
    
    passed_tests = 0
    total_tests = len(test_cases)

    for test_input, expected_output in test_cases:
        # Prepend the test input to the code if needed (e.g., input via arguments)
        full_code = content  # Modify this if test_input should be part of the code
        
        output = run_code_in_docker(full_code, language)
        
        if output.strip() == expected_output.strip():
            st.success(f"Test Passed: Input: {test_input}")
            passed_tests += 1
        else:
            st.error(f"Test Failed: Input: {test_input}, Expected: {expected_output}, Got: {output}")

    st.write(f"Passed {passed_tests}/{total_tests} test cases.")
