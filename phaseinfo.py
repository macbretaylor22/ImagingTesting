import pydicom
file_path = "~/Projects/s007_bravo-250_07222026/s007_bravo/IM_0001.dcm"
def extract_standard_timing(file_path):
    ds = pydicom.dcmread(file_path)
    print(f"--- Timing Data for: {file_path} ---")
    
    # Check if Multi-frame or Single-frame
    if "PerFrameFunctionalGroupsSequence" in ds:
        print("[Format] Enhanced Multi-frame DICOM detected")
        # Grab timing for the first frame as a reference
        frame_0 = ds.PerFrameFunctionalGroupsSequence[0]
        
        # Look for Cardiac/Temporal synchronization macros
        if "CardiacSynchronizationSequence" in frame_0:
            cardiac = frame_0.CardiacSynchronizationSequence[0]
            print(f"Nominal Trigger Delay: {cardiac.get((0x0020, 0x9153), 'N/A').value} ms")
        if "FrameContentSequence" in frame_0:
            content = frame_0.FrameContentSequence[0]
            print(f"Temporal Position Index: {content.get((0x0020, 0x9128), 'N/A').value}")
            
    else:
        print("[Format] Standard Single-frame DICOM detected")
        # Direct fallback queries on standard root tags
        trigger_time = ds.get((0x0018, 0x1060), None)
        temporal_res = ds.get((0x0020, 0x0110), None)
        phase_index = ds.get((0x0020, 0x0128), None)
        
        print(f"Trigger Time: {trigger_time.value if trigger_time else 'N/A'} ms")
        print(f"Temporal Resolution: {temporal_res.value if temporal_res else 'N/A'} ms")
        print(f"Temporal Phase Index: {phase_index.value if phase_index else 'N/A'}")

# Usage
# extract_standard_timing("your_image.dcm")
