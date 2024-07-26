-- StarterGui/PlayerGui: MainScript

-- Create ScreenGui for the GUI
local gui = Instance.new("ScreenGui")
gui.Name = "FreezeGUI"
gui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")

-- Create Frame for the GUI
local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 200, 0, 150)
frame.Position = UDim2.new(0.75, -100, 0.75, -75) -- Adjust position as needed
frame.BackgroundColor3 = Color3.new(0.2, 0.2, 0.2)
frame.Active = true
frame.Draggable = true
frame.Parent = gui

-- Add cyan outline to the frame
local uiStroke = Instance.new("UIStroke")
uiStroke.Color = Color3.fromRGB(0, 255, 255) -- Cyan color
uiStroke.Thickness = 2
uiStroke.Parent = frame

-- Create Title Label for the GUI
local titleLabel = Instance.new("TextLabel")
titleLabel.Size = UDim2.new(1, 0, 0, 30)
titleLabel.Position = UDim2.new(0, 0, 0, 0)
titleLabel.BackgroundColor3 = Color3.new(0.3, 0.3, 0.3)
titleLabel.Text = "Freeze GUI"
titleLabel.Font = Enum.Font.SourceSansBold
titleLabel.TextSize = 18
titleLabel.TextColor3 = Color3.new(1, 1, 1)
titleLabel.Parent = frame

-- Create Close Button for the GUI
local closeButton = Instance.new("TextButton")
closeButton.Size = UDim2.new(0, 30, 0, 30)
closeButton.Position = UDim2.new(1, -35, 0, 5)
closeButton.BackgroundColor3 = Color3.new(0.2, 0.2, 0.2)
closeButton.Text = "X"
closeButton.Font = Enum.Font.SourceSansBold
closeButton.TextSize = 24
closeButton.TextColor3 = Color3.new(1, 1, 1)
closeButton.Parent = frame

-- Create Freeze/Unfreeze Button for the GUI
local freezeButton = Instance.new("TextButton")
freezeButton.Size = UDim2.new(0, 180, 0, 30)
freezeButton.Position = UDim2.new(0.5, -90, 0.5, -45)
freezeButton.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
freezeButton.Text = "Freeze"
freezeButton.Font = Enum.Font.SourceSansBold
freezeButton.TextSize = 18
freezeButton.TextColor3 = Color3.fromRGB(255, 255, 255)
freezeButton.Parent = frame

-- Functionality for Close Button
closeButton.MouseButton1Click:Connect(function()
    gui:Destroy()
end)

-- Functionality for Freeze/Unfreeze Button
local frozen = false
freezeButton.MouseButton1Click:Connect(function()
    local player = game.Players.LocalPlayer
    local character = player.Character

    if character then
        local humanoid = character:FindFirstChildOfClass("Humanoid")

        if humanoid then
            frozen = not frozen
            if frozen then
                -- Freeze player
                humanoid.WalkSpeed = 0
                humanoid.JumpPower = 0
                humanoid.PlatformStand = true
                for _, part in pairs(character:GetChildren()) do
                    if part:IsA("BasePart") then
                        part.Anchored = true
                    end
                end
                freezeButton.Text = "Unfreeze"
            else
                -- Unfreeze player
                humanoid.WalkSpeed = 16 -- Default walk speed
                humanoid.JumpPower = 50 -- Default jump power
                humanoid.PlatformStand = false
                for _, part in pairs(character:GetChildren()) do
                    if part:IsA("BasePart") then
                        part.Anchored = false
                    end
                end
                freezeButton.Text = "Freeze"
            end
        end
    end
end)
