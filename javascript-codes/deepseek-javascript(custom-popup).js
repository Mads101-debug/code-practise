








                        window.addEventListener('load', () => {
                            setTimeout(() => {
                                alert('This page is under construction 🔨');
                            }, 50);
                        });


















                        window.addEventListener('load', () => {
                            setTimeout(() => {
                                // Create custom alert element
                                const customAlert = document.createElement('div');
                                customAlert.textContent = 'This appears 1 second after page load!';
                                customAlert.style.cssText = `
                                    position: fixed;
                                    top: 20px;
                                    right: 20px;
                                    background: #333;
                                    color: white;
                                    padding: 15px;
                                    border-radius: 5px;
                                    z-index: 1000;
                                `;
                                
                                // Add to page
                                document.body.appendChild(customAlert);
                                
                                // Auto-remove after 2 seconds
                                setTimeout(() => {
                                    customAlert.remove();
                                }, 2000);
                            }, 50);
                        });
