import streamlit as st
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
import time
    
def response_generator():
    response = """
**1. Ownership of Intellectual Property**

**Clause Example:**

*“All intellectual property rights, including but not limited to patents, trademarks, copyrights, trade secrets, and proprietary information, shall remain the sole property of [Company Name]. No rights, title, or interest in the intellectual property shall be transferred to the buyer, except as explicitly provided in this agreement.”*

**Recommendation:**

Ensure that this clause is present in all contracts, particularly those involving proprietary technology, designs, or software.

**2. Limited License for Use**

**Clause Example:**

*“The Buyer is granted a non-exclusive, non-transferable, revocable license to use the [product/software/design] solely for its intended purpose and in accordance with this Agreement. Any reproduction, modification, reverse engineering, or distribution of the intellectual property is strictly prohibited without prior written consent from [Company Name].”*

**Recommendation:**

Add detailed limitations to the license to prevent misuse or unauthorized redistribution of your IP."""

    for word in response.splitlines():
        yield word + "\n"
        time.sleep(0.05)
        
def chatbot():
    if not st.session_state['authenticated']:
        st.warning("Please log in to access this page.")
    else:
        
        st.title("ContractGPT Chatbot")
        if "messages" not in st.session_state:
            st.session_state.messages = []


        # React to user input
        in1=st.chat_input()
        if in1:
            st.chat_message("user").markdown(in1)
            st.session_state.messages.append({"role": "user", "content": in1})
            response_container = st.chat_message("assistant").empty()  # Create a placeholder for the assistant's response
            assistant_response = ""
            
            for word in response_generator():
                assistant_response += word  # Build the response as we go
                response_container.markdown(assistant_response)  # Update the response container incrementally
                        # Append the assistant's response to session state messages
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
chatbot()